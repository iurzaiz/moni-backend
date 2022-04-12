//----------------------------------------------------------------------
//                        CONFIGURACION
//----------------------------------------------------------------------
const host = "http://localhost:8000";
//----------------------------------------------------------------------
//                   FIN DE LA CONFIGURACION
//----------------------------------------------------------------------


// VARIABLES

/*----------------------------------------------------------------------
 Esta funcion permite ingresar al sistema y almacenar los access y refresh
 token en el navegador
------------------------------------------------------------------------*/

function Login(){
		email= $('#txtEmail').val()
		password= $('#txtPassword').val()
		lastDate = new Date();
		var formdata = new FormData();
		formdata.append("email", email);
		formdata.append("password", password);

		var requestOptions = {
		method: 'POST',
		body: formdata,
		redirect: 'follow'
		};

		fetch(host+"/api/token/", requestOptions)
		.then(response => response.text())
		.then(result => {
			res = JSON.parse(result);
			if (res.refresh!=undefined){
				console.log("guardo tokens")
				GuardarTokens(res.access, res.refresh, lastDate);
				
				

			}else{
				alert("user o pass incorrect")
			}
			})
		.catch(error => console.log('error', error));
	
}

/*----------------------------------------------------------------------
 Esta funcion permite guardar los tokens que genera el inicio de sesión
------------------------------------------------------------------------*/
function GuardarTokens(access, refresh, lastDate){
	window.localStorage.setItem('access_token', access);
	window.localStorage.setItem('refresh_token', refresh);
	window.localStorage.setItem('lastDate', lastDate);
	console.log("token guardados ", access, "  ", refresh);
	window.location.href="./admin.html"
}

/*----------------------------------------------------------------------
 Esta funcion chequea la existencia de los tokens
------------------------------------------------------------------------*/
function ChequearExistenciaTokens(){
	if ((localStorage.getItem('access_token')===null) || 
	(localStorage.getItem('refresh_token')===null)){
		return false;
	}else{
		return true;
	}
}

/*----------------------------------------------------------------------
 Esta funcion permite validar campos solicitud

------------------------------------------------------------------------*/
function ValidarSolicitud(){
	nombre= $('#txtNombre').val();
	apellido= $('#txtApellido').val();
	dni= $('#txtDni').val();
	email= $('#txtEmail').val();
	genero=$('#cmbSexo').val();
	monto=$('#txtMonto').val();
	
	if (nombre.trim() ==""){
		$('#txtNombre').css("position", "relative")
		$('#txtNombre').css("background-color", "#ffdddd")
		.animate({ left: "-10px" }, 100).animate({ left: "10px" }, 100)
		.animate({ left: "-10px" }, 100).animate({ left: "10px" }, 100)
		.animate({ left: "0px" }, 100);

		alert("El campo nombre está vacío")
		return
	}else{
		$('#txtNombre').css("background-color", "#fff")
	}

	if (apellido.trim() ==""){
		$('#txtApellido').css("position", "relative")
		$('#txtApellido').css("background-color", "#ffdddd")
		.animate({ left: "-10px" }, 100).animate({ left: "10px" }, 100)
		.animate({ left: "-10px" }, 100).animate({ left: "10px" }, 100)
		.animate({ left: "0px" }, 100);

		alert("El campo apellido está vacío")
		return
	}else{
		$('#txtApellido').css("background-color", "#fff")
	}

	if (email.trim() ==""){
		$('#txtEmail').css("position", "relative")
		$('#txtEmail').css("background-color", "#ffdddd")
		.animate({ left: "-10px" }, 100).animate({ left: "10px" }, 100)
		.animate({ left: "-10px" }, 100).animate({ left: "10px" }, 100)
		.animate({ left: "0px" }, 100);

		alert("El campo email está vacío")
		return
	}else{
		$('#txtEmail').css("background-color", "#fff")
	}
	

	if (parseInt(dni)<=1000000 || parseInt(dni)>=100000000){
		$('#txtDni').css("background-color", "#fff")
		$('#txtDni').css("position", "relative")
		$('#txtDni').css("background-color", "#ffdddd")
		.animate({ left: "-10px" }, 100).animate({ left: "10px" }, 100)
		.animate({ left: "-10px" }, 100).animate({ left: "10px" }, 100)
		.animate({ left: "0px" }, 100);

		alert("El campo dni no es valido")
		return
	}else{
		$('#txtDni').css("background-color", "#fff")
	}
	
	if (isNaN(monto)){

		$('#txtMonto').css("background-color", "#fff")

		$('#txtMonto').css("position", "relative")
		$('#txtMonto').css("background-color", "#ffdddd")
		.animate({ left: "-10px" }, 100).animate({ left: "10px" }, 100)
		.animate({ left: "-10px" }, 100).animate({ left: "10px" }, 100)
		.animate({ left: "0px" }, 100);

		alert("El campo monto está vacío o no es valido")
		return
	}else{
		$('#txtMonto').css("background-color", "#fff")
		
	}
	RegistrarSolicitud(dni, nombre, apellido, genero, email, monto)

}

/*----------------------------------------------------------------------
 Esta funcion permite registrar unasolicitud
------------------------------------------------------------------------*/
function RegistrarSolicitud(dni, nombre, apellido, genero, email, monto){
	

	var formdata = new FormData();
	 formdata.append('dni', dni);
	 formdata.append('nombre', nombre);
	 formdata.append('apellido', apellido);
	 formdata.append('genero', genero);
	 formdata.append('email', email);
	 formdata.append('monto', monto);

	var requestOptions = {
	 	method: 'POST',
	 	body: formdata,
	   };
	  
	   fetch(host + "/api/solicitudes/solicitudes/", requestOptions)
	 	.then(response => response.text())
	 	.then(function(){
			window.alert("Solicitud registrada")
	 		location.reload()
	 	})
	 	.catch(error => window.alert('Hubo un error: '+ error));

}

/*----------------------------------------------------------------------
 Esta funcion permite listar las solicitudes, consumiendo servicio de API
------------------------------------------------------------------------*/

function ListarSolicitudes(){
	header = new Headers()
	header.append('Authorization', 'Bearer ' + localStorage.getItem('access_token'))

	var requestOptions = {
		method: 'GET',
		//headers: header,
		//mode: 'no-cors',
	};

	fetch(host+"/api/solicitudes/solicitudes/",requestOptions)
		// .then(response => {
		// 	response.text()
		// 	if(response.status!==401){
		// 		//window.location.href="./login.html"
		// 	}
		// 	if(response.status!==200){
		// 		alert("hubo un error al cargar las solicitudes")
		// 	}
			
		// })
		.then(response => response.text())
		.then(result => {
			res = JSON.parse(result)
			var contenido = "";

			for (var i=0; i< res.length; i++)
			{
				var s = res[i];
                contenido += ('<tr>'+
                                    '<td>'+s.dni+'</td>'+
                                    '<td>'+s.nombre+'</td>'+
                                    '<td>'+s.apellido+'</td>'+
                                    '<td>'+s.monto+'</td>'+
                                    '<td>'+s.email+'</td>'+
                                    '<td>'+s.genero+'</td>'+
                                    '<td>'+s.estaAprobado+'</td>'+
									'<td><button onclick="'+"EditarSolicitud("+s.id+")"+'" class="btn btn-info">Editar</button></td>'+
                                    '<td><button onclick="'+"EliminarSolicitud("+s.id+")"+'" class="btn btn-danger btnEliminar">Eliminar</button></td>'+
									
                                '</tr>')
			}
			
			$('#ContenidoTabla').append(contenido);
					
		})
		.catch(error => console.log('error', error)); 
		
}

/*----------------------------------------------------------------------
 La siguiente funcion elimina la solicitud seleccionada
------------------------------------------------------------------------*/
function EliminarSolicitud(id){

	if (window.confirm("Seguro que desea eliminar la solicitud?")==true){
		var formdata = new FormData();

		var requestOptions = {
			method: 'DELETE',
			body: formdata,
			redirect: 'follow'
		};

		fetch(host+'/api/solicitudes/solicitudes/'+id, requestOptions)
			.then(response => response.json())
			.then(function(){	
				alert("solicitud eliminada")
				window.location.href= "./admin.html"
			})
			.catch(error => console.log('error', error));
	
	}
	else{
		return
	}
}

/*----------------------------------------------------------------------
 La siguiente funcion redirije a la pagina
------------------------------------------------------------------------*/
function EditarSolicitud(id){
	window.location.href='./edit.html?id='+id
}


/*----------------------------------------------------------------------
 Esta funcion rellena los campos de la pagina mi perfil"
------------------------------------------------------------------------*/
function RellenarCamposSolicitud(){

	var id = getParameterByName('id');
	var requestOptions = {
		method: 'GET',
		};
	fetch(host +"/api/solicitudes/solicitudes/"+id, requestOptions)
	.then(response => response.text())
	.then(result => {
		s = JSON.parse(result)

		$('#txtNombre').val(s.nombre);
		$('#txtApellido').val(s.apellido);
		$('#txtDni').val(s.dni);
		$('#txtEmail').val(s.email);
		$('#cmbSexo').val(s.genero);
		$('#txtMonto').val(s.monto);
		$('#cmdEstaAprobado').val(s.estaAprobado);	
	})
	.catch(error => console.log('error', error));
}

/*----------------------------------------------------------------------
 Esta funcion obtiene el parametro de la url
------------------------------------------------------------------------*/
function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
    results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

/*----------------------------------------------------------------------
 Esta funcion edita la solicitud
------------------------------------------------------------------------*/

function SubmitEditarSolicitud(){ 
	id = getParameterByName('id');
	nombre= $('#txtNombre').val();
	apellido= $('#txtApellido').val();
	dni= $('#txtDni').val();
	email= $('#txtEmail').val();
	genero=$('#cmbSexo').val();
	monto=$('#txtMonto').val();
	estaAprobado=$('#cmbEstaAprobado').val();
	
	if (isNaN(monto)){
		$('#txtMonto').css("background-color", "#fff")

		$('#txtMonto').css("position", "relative")
		$('#txtMonto').css("background-color", "#ffdddd")
		.animate({ left: "-10px" }, 100).animate({ left: "10px" }, 100)
		.animate({ left: "-10px" }, 100).animate({ left: "10px" }, 100)
		.animate({ left: "0px" }, 100);

		alert("El campo monto está vacío o no es valido")
		return
	}else{
		$('#txtMonto').css("background-color", "#fff")
		
	}

	var formdata = new FormData();
	formdata.append('id', id);
	formdata.append('dni', dni);
	formdata.append('nombre', nombre);
	formdata.append('apellido', apellido);
	formdata.append('genero', genero);
	formdata.append('email', email);
	formdata.append('monto', monto);
	formdata.append('estaAprobado', estaAprobado);

	var requestOptions = {
		method: 'PUT',
		body: formdata,
		redirect: 'follow'
	};

	fetch(host + "/api/solicitudes/solicitudes/"+id, requestOptions)
	.then(response => response.text())
	.then(function(){
		window.alert("solicitud modificada")
		window.location.href='./admin.html';
	})
	.catch(error => {
		console.log('error', error)
		window.alert("No se pudo modificar la solicitud")
	});

}


