def urlval():
	import requests
	import clr
	from System.Net import ServicePointManager, SecurityProtocolType
	ServicePointManager.ServerCertificateValidationCallback = lambda sender, certificate, chain, sslPolicyErrors: True
	ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls | SecurityProtocolType.Ssl3 | SecurityProtocolType.Tls11 | SecurityProtocolType.Tls12
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
	requests.packages.urllib3.disable_warnings()
	requests.verify=False
	request = requests.get('https://blogs.infosupport.com')
	'''request = requests.get('http://google.com')'''
	if request.status_code == 200:
		a = "Web site exists"
		RETURN (a);
	else:
		a = "Web site does not exist"
		RETURN (a);
urlval()


