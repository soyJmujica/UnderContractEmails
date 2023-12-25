
function guardarPDF(){
                      // Obtén el contenido HTML de los divs
          var contenidoDiv1 = document.getElementById("div1").innerHTML;
          var contenidoDiv2 = document.getElementById("div2").innerHTML;
          var contenidoDiv3 = document.getElementById("div3").innerHTML;
          var contenidoDiv4 = document.getElementById("div4").innerHTML;
          var contenidoDiv5 = document.getElementById("div5").innerHTML;
          var contenidoDiv6 = document.getElementById("div6").innerHTML;
          var contenidoDiv7 = document.getElementById("div7").innerHTML;
          var contenidoDiv8 = document.getElementById("div8").innerHTML;
          var contenidoDiv9 = document.getElementById("div9").innerHTML;

          // Crea un nuevo objeto jsPDF
          var pdf = new jsPDF();

          // Agrega el contenido HTML al PDF
          doc.fromHTML(contenidoDiv1, 10, 10);
          //guardar pdf
          doc.save("archivo.pdf");
          doc.fromHTML(contenidoDiv2, 10, 10);
          //guardar pdf
          doc.save("archivo.pdf");
          doc.fromHTML(contenidoDiv3, 10, 10);
          //guardar pdf
          doc.save("archivo.pdf");
          doc.fromHTML(contenidoDiv4, 10, 10);
          //guardar pdf
          doc.save("archivo.pdf");
          doc.fromHTML(contenidoDiv5, 10, 10);
          //guardar pdf
          doc.save("archivo.pdf");
          doc.fromHTML(contenidoDiv6, 10, 10);
          //guardar pdf
          doc.save("archivo.pdf");
          doc.fromHTML(contenidoDiv7, 10, 10);
          //guardar pdf
          doc.save("archivo.pdf");
          doc.fromHTML(contenidoDiv8, 10, 10);
          //guardar pdf
          doc.save("archivo.pdf");
          doc.fromHTML(contenidoDiv9, 10, 10);
          //guardar pdf
          doc.save("archivo.pdf")

          

}