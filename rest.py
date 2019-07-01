#pip install requests

import requests

resp = requests.get('http://192.168.0.104:8080/calculetterest/calc/add/7/8')
if resp.status_code == 200:
    # This means something went wrong.
    print(resp.text)

    with open(ficher_pdf, 'w') as f:
    	f.resp


    
else:
	raise ApiError('Erreur :{}'.format(resp.status_code))

#http://192.168.0.104:8080/calculetterest/calc/getPdf