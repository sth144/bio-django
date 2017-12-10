function clickCopy() {
  var text = document.getElementById("output");
  text.select();
  document.execCommand("Copy");
  alert("Copied the text: " + text.value);
}
