const buttons = document.querySelectorAll(".btn");
const display = document.getElementById("display");
const secondaryDisplay = document.getElementById("secondary-display");

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    const value = button.getAttribute("data-value");

    if (value === "C") {
      display.value = "";
      secondaryDisplay.value = "";
    } else if (value === "=") {
      try {
        secondaryDisplay.value = display.value + " = " + eval(display.value);
        display.value = eval(display.value);
      } catch {
        display.value = "Error";
      }
    } else {
      display.value += value;
      secondaryDisplay.value = display.value;
    }
  });
});
