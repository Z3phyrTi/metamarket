(function (d, w) {
	const rutas = {
		'/login': {
			archivo: 'login.html',
			hacer: function () {
				console.log('');
			},
			
		},
		'/carrito': {
			archivo: 'carrito.html',
			hacer: function () {
				console.log('');
			}         
		}
	};
	const contenedor = document.getElementById('contenido-web');
	d.addEventListener('readystatechange', function () {
		if (d.readyState === 'interactive') {
			// aquí va el codigo de arranque de mi app.
			iniciarTodo();
		}
	});

	function iniciarTodo() {
		w.addEventListener('hashchange', function () {
			// Borro el # de inicio
			const ruta = w.location.hash;
			cargarArchivoDeUnaRuta(ruta);
			// console.log(rutas[ruta]);
		});
		cargarArchivoDeUnaRuta(w.location.hash);
	}

	function cargarArchivoDeUnaRuta(rutaACargar) {
		const ruta = rutas[rutaACargar.substring(1)];
		fetch(`${w.location.origin}/paginas/${ruta.archivo}`, {
			method: 'GET',
		})
			.then(function (respuesta) {
				return respuesta.text();
			})
			.then(function (respuestaTexto) {
				contenedor.innerHTML = '';
				contenedor.innerHTML = respuestaTexto;
				ruta.hacer();
			});
	}

	// la ruta del navegador, parametros, function despues de ..., etc
	// la ruta del navegador, archivo que dega cargar (html)
})(document, window);
