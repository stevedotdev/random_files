function decrypt() {
  const inputText = document.getElementById("input").value;
  let decryptedText = "";

  for (let i = 0; i < inputText.length; i++) {
    let charCode = inputText.charCodeAt(i);

    if (charCode >= 65 && charCode <= 90) {
      // A-Z
      charCode = ((charCode - 65 + 13) % 26) + 65;
    } else if (charCode >= 97 && charCode <= 122) {
      // a-z
      charCode = ((charCode - 97 + 13) % 26) + 97;
    }

    decryptedText += String.fromCharCode(charCode);
  }

  document.getElementById("output").value = decryptedText;
}
