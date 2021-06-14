function buy() {
	let myElement = document.querySelector(".buyform");
	myElement.style.display = 'block';
	let show_btn = document.querySelector("#calcbtn1")
	show_btn.style.display = 'block';
}



function buy_calc () {

	
	let rmv_none = document.querySelector(".reasult_buy");
	rmv_none.style.display = 'block';

	var reas_;
	//Storing values for different charge ranges!
	k = 50000
	l = 500000
	m = 2000000
	n = 10000000
	o = 1000000000

	var bp =  document.getElementById("formGroupExampleInput").value;
	var quantity =  document.getElementById("formGroupExampleInput2").value;
	var purchase = parseInt(bp)* parseInt(quantity);
	
	if (k >= purchase){
		reas_ = purchase*0.004;
	}else if (l >= purchase ){
		reas_ = purchase * 0.0037;
	}else if (m >= purchase){
		reas_ = purchase * 0.0034;
	}else if (n >=purchase ){
		reas_ = purchase * 0.003;
	}else if (o >= purchase){
		reas_ = purchase * 0.0027;
	}
	var sebo_commi = purchase * 0.00015;
	var dp_charge = 25;
	var total_amount = purchase + reas_ + dp_charge + sebo_commi
	var ppc = total_amount/quantity;
	var purchase_commission = document.getElementById("pv");
	purchase_commission.innerText = purchase;

	var purchase_volume = document.getElementById("bc");
	purchase_volume.innerText = reas_;
	
	var broken_commision = document.getElementById("sc");
	broken_commision.innerText = sebo_commi;
	
	var dp_ch = document.getElementById("dp");
	dp_ch.innerText = dp_charge;

	var price_per_unit = document.getElementById("pps");
	price_per_unit.innerText = ppc;

	var total = document.getElementById("ta");
	total.innerText = total_amount;

	var bt = document.getElementById('calcbtn');
	// bt.onclick = window.location.reload();	

}

