function buy() {
	let myElement = document.querySelector(".buyform");
	myElement.style.display = 'block';
}

function buy_calc () {
	//making none to block;


	//getting the two input from form
	var bp =  document.getElementById("formGroupExampleInput").value;
	var quantity =  document.getElementById("formGroupExampleInput2").value;
	var purchase = parseInt(bp)* parseInt(quantity); //calculating purchase
	var reas_;
	//Storing values for different charge ranges!
	k = 50000
	l = 500000
	m = 2000000
	n = 10000000
	o = 1000000000

	if (k >= purchase){
		reas_ = purchase*0.004;
	};

	else if (l >= purchase){
		reas_ = purchase * 0.0037;
	};

	else if (m >= ){
		reas_ = purchase * 0.0034;
	};

	else if (n >=purchase ){
		reas_ = purchase * 0.003;
	};

	else if (o >= purchase){
		reas_ = purchase * 0.0027;
	};


	var sebo_commi = 25 * 0.00015;
	var dp_charge = 25;
	var total_amount = purchase + reas_ + dp_charge + sebo_commi
	var purchase_commission = document.getElementById("pv");
	purchase_commission.append(purchase);

	var purchase_volume = document.getElementById("bc");
	purchase_volume.append(reas_);
	
	var broken_commision = document.getElementById("sc");
	broken_commision.append(sebo_commi);
	
	var total_amount = document.getElementById("ta");
	total_amount.append(total_amount);

	var bt = document.getElementById('calcbtn');
	// bt.onclick = window.location.reload();

}
