import requests


class sheet_manager():

    def __init__(self, url):
        self.url = url

    def get_all_data(self, tab_name=None):
        url = self.url
        if tab_name is not None:
            url = self.url + "/tabs/"+tab_name

        response = requests.get(url)
        if response.status_code == 200:
            response_data = response.json()
        else:
            if response.status_code == 402:
                return {
                "Status": False,
                "Message": "API CONSUMPTION LIMIT REACHED",
                "Error": response.text
                }
            return {
                "Status": False,
                "Message": "An error occurred.",
                "Error": response.text
            }
        
        return {
            "Status": True,
            "Message": "Data retrieval successful.",
            "Data": response_data
        }

    def send_data(self, data, tab_name=None):
        url = self.url
        if tab_name is not None:
            url = self.url + "/tabs/"+tab_name
        
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return {
                "Status": True,
                "Message": "Data saved successfully."
            }
        else:
            if response.status_code == 402:
                return {
                "Status": False,
                "Message": "API CONSUMPTION LIMIT REACHED",
                "Error": response.text
                }
            return {
                "Status": False,
                "Message": "An error occurred.",
                "Error": response.text
            }
    
    def delete_data(self, row_number, tab_name=None):
        url = self.url
        if tab_name is not None:
            url = self.url + "/tabs/"+tab_name
        
        response = requests.delete(url+"/"+str(row_number-2))
        if response.status_code == 200:
            return {
                "Status": True,
                "Message": "Data deleted successfully."
            }
        else:
            if response.status_code == 402:
                return {
                "Status": False,
                "Message": "API CONSUMPTION LIMIT REACHED",
                "Error": response.text
                }
            return {
                "Status": False,
                "Message": "An error occurred.",
                "Error": response.text
            }

    def delete_filtered_data(self, column_name, data, tab_name=None):
        url = self.url
        if tab_name is not None:
            url = self.url + "/tabs/"+tab_name

        response = requests.delete(url+"/"+str(column_name)+"/*"+str(data)+"*")
        if response.status_code == 200:
            return {
                "Status": True,
                "Message": "Data deleted successfully."
            }
        else:
            if response.status_code == 402:
                return {
                "Status": False,
                "Message": "API CONSUMPTION LIMIT REACHED",
                "Error": response.text
                }
            return {
                "Status": False,
                "Message": "An error occurred.",
                "Error": response.text
            }

    def update_row(self, row_number, data, tab_name=None):
        url = self.url
        if tab_name is not None:
            url = self.url + "/tabs/"+tab_name

        response = requests.put(url+"/"+str(row_number-2), json=data)
        if response.status_code == 200:
            return {
                "Status": True,
                "Message": "Data updated successfully."
            }
        else:
            if response.status_code == 402:
                return {
                "Status": False,
                "Message": "API CONSUMPTION LIMIT REACHED",
                "Error": response.text
                }
            return {
                "Status": False,
                "Message": "An error occurred.",
                "Error": response.text
            }

    def update_fields(self, row_number, data, tab_name=None):
        url = self.url
        if tab_name is not None:
            url = self.url + "/tabs/"+tab_name
            
        response = requests.patch(url+"/"+str(row_number-2), json=data)
        if response.status_code == 200:
            return {
                "Status": True,
                "Message": "Data updated successfully."
            }
        else:
            if response.status_code == 402:
                return {
                "Status": False,
                "Message": "API CONSUMPTION LIMIT REACHED",
                "Error": response.text
                }
            return {
                "Status": False,
                "Message": "An error occurred.",
                "Error": response.text
            }
    
