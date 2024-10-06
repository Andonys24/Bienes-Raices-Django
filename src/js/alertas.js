(function () {
	alertas = document.querySelectorAll(".alerta");
	alertas.forEach((alerta) => {
		if (alerta) {
			setTimeout(() => {
				alerta.remove();
			}, 5000);
		}
	});
})();
