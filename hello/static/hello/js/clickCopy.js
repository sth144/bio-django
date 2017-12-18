/*****************************************************
	Title: clickCopy() Function Definition
	Author: Sean Hinds
	Date: 12/17/17
	Description: Can be set as onclick functionality
					of a DOM element to copy text
					in output field to the user's
					clipboard
*****************************************************/


// clickCopy() function definition. To be executed by
// 	the client browser.

function clickCopy() {

	// target the output box
	var text = document.getElementById("output");

	// select the text
  	text.select();

  	// copy to clipboard
  	document.execCommand("Copy");

}
