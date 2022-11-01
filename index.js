async function main() {
	var x = document.getElementsByClassName("text-secondary duration-250 tabular-nums transition-colors text-3xl");
	console.log(x[0].style.color);
	if (x[0].style.color == "rgb(160, 160, 160)") {
		var y = document.getElementsByClassName("inline-flex items-center justify-center  bg-badge-neutral text-badge-neutral text-xs h-5 px-1.5 rounded-md tabular-nums");
		console.log(x[0].innerText);
		y[0].innerText = "MY TURN"
	} else {
		var y = document.getElementsByClassName("inline-flex items-center justify-center  bg-badge-neutral text-badge-neutral text-xs h-5 px-1.5 rounded-md tabular-nums");
		console.log(x[0].innerText);
		y[0].innerText = "YOUR TURN"
	}
}

setInterval(main,2000);