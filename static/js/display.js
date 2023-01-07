function toggleVisibility(arg) {
  var xs = document.getElementsByClassName(arg);
  var btn = document.getElementById(arg+"-button");
  //var att = document.createAttribute("disabled");
  //btn.setAttributeNode(att);
  btn.classList.toggle("grayed-out");

  for (i = 0; i < xs.length; i++) {
    if (xs[i].style.display === "none") {
      xs[i].style.display = "inline-block";
    } else {
      xs[i].style.display = "none";
    }
  }
}

function cv2pdf() {
  // Default export is a4 paper, portrait, using milimeters for units
  var doc = new jsPDF();

  doc.text('Przepraszam, jeszcze nad tym pracuje', 10, 10);
  doc.save('Krzysztof_Kokosinski_CV.pdf');
}
