// Переменные с данными пользователя
var isWorking = true;
var isRightsEnabled = true;  // если права не нужны, поставьте false
var isCovidCertificateEnabled = true;  // если COVID-сертификат не нужен, поставьте false

var fullname = "Бабаков Лука Сергеевич";
var name = "Лука";
var birthdate = "05.09.2011";
var passport_id = "520471839";
var kpp_id = "05098251420";

// Данные для водительских прав (если isRightsEnabled = true)
var rights_valid_until = "01.01.2022";
var rights_categories = "A, B";
var rights_tsc = "ТСЦ 8631";
var rights_id = "KBE968639";

// Данные для COVID-сертификата (если isCovidCertificateEnabled = true)
var covid_valid_until = "11.03.2022";
var covid_certificate_id = "URN:UVCI:01:UA:0E55669376876888B9E2520C4F88930";

if(isWorking) {
	for(el of document.getElementsByClassName("birthdate")){
		el.innerHTML = "Дата народження: " + birthdate;
	}
	for(el of document.getElementsByClassName("fullname")){
		el.innerHTML = fullname;
	}
	document.getElementsByClassName("menutitile")[0].innerHTML = "Вітаємо, " + name;
	document.getElementsByClassName("passport_id")[0].innerHTML = "Номер: " + passport_id;

	document.getElementsByClassName("kpp_id")[0].innerHTML = kpp_id;

	if(isRightsEnabled) {
		document.getElementsByClassName("rights_valid_until")[0].innerHTML = "Дійсне до: " + rights_valid_until;
		document.getElementsByClassName("rights_categories")[0].innerHTML = "Категорії: " + rights_categories;
		document.getElementsByClassName("rights_tsc")[0].innerHTML = "Видав: " + rights_tsc;
		document.getElementsByClassName("rights_id")[0].innerHTML = rights_id;
	}

	if(isCovidCertificateEnabled) {
		document.getElementsByClassName("covid_valid_until")[0].innerHTML = "Дійсний до: " + covid_valid_until;
		document.getElementsByClassName("covid_certificate_id")[0].innerHTML = covid_certificate_id;
	}
}
