import path from 'path';
import fs from 'fs';
import { glob } from 'glob';
import { src, dest, watch, series } from 'gulp';
import gulpPlumber from 'gulp-plumber';
import * as dartSass from 'sass';
import gulpSass from 'gulp-sass';
import concat from 'gulp-concat';
import terser from 'gulp-terser';
import sharp from 'sharp';
import rename from 'gulp-rename';

const sass = gulpSass(dartSass);

const paths = {
    scss: 'src/scss/**/*.scss',
    js: 'src/js/**/*.js'
};

export function css() {
    return src(paths.scss, { sourcemaps: true })
        .pipe(gulpPlumber())
        .pipe(sass({
            outputStyle: 'compressed'
        }).on('error', sass.logError))
        .pipe(dest('./bienes_raices/static/css', { sourcemaps: '.' }));
}

export function js() {
    return src(paths.js)
        .pipe(concat('bundle.js'))
        .pipe(terser())
        .pipe(rename({ suffix: '.min' }))
        .pipe(dest('./bienes_raices/static/js'));
}

async function imagenes() {
    const srcDir = './src/img';
    const buildDir = './bienes_raices/static/img';
    const images = await glob('./src/img/**/*');
    await Promise.all(images.map(async file => {
        const relativePath = path.relative(srcDir, path.dirname(file));
        const outputSubDir = path.join(buildDir, relativePath);
        await procesarImagenes(file, outputSubDir);
    }));
}

async function procesarImagenes(file, outputSubDir) {
    if (!fs.existsSync(outputSubDir)) {
        fs.mkdirSync(outputSubDir, { recursive: true });
    }
    const baseName = path.basename(file, path.extname(file));
    const extName = path.extname(file);

    if (extName.toLowerCase() === '.svg') {
        const outputFile = path.join(outputSubDir, `${baseName}${extName}`);
        fs.copyFileSync(file, outputFile);
    } else {
        const outputFile = path.join(outputSubDir, `${baseName}${extName}`);
        const outputFileWebp = path.join(outputSubDir, `${baseName}.webp`);
        const outputFileAvif = path.join(outputSubDir, `${baseName}.avif`);
        const options = { quality: 80 };

        await Promise.all([
            sharp(file).jpeg(options).toFile(outputFile),
            sharp(file).webp(options).toFile(outputFileWebp),
            sharp(file).avif().toFile(outputFileAvif)
        ]);
    }
}

export function dev() {
    watch(paths.scss, { usePolling: true, interval: 3000 }, css);
    watch(paths.js, { usePolling: true, interval: 3000 }, js);
    watch('src/img/**/*.{png,jpg}', { usePolling: true, interval: 3000 }, imagenes);
}


export default series(js, css, imagenes, dev);