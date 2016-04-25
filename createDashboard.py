# Now, create a dashboard
import requests, json

# Takes in a list of string URLs, a string date, and a string time_type, and returns a link to the dashboard
class createDashboard:
    def __init__(self, graph_URLs, date_range):
        self.date_range = date_range
        self.graph_URLs = graph_URLs

        # Order of graphs
        self.rows_list = []
        for URL in graph_URLs:
            self.rows_list.append([{"plot_url" : URL}])

        self.banner_title = ""
        self.create_banner()
        self.generate()


    # Convert "date" to "date (time_type)"
    def create_banner(self):
        self.banner_title += self.date_range[0]
        self.banner_title += " to "
        self.banner_title += self.date_range[1]


    # Calls API to generate a link to the dashboard
    def generate(self):
        dashboard_json = {
            "rows": self.rows_list,
            "banner": {
                "visible": True,
                "backgroundcolor": "#3d4a57",
                "textcolor": "white",
                "title": self.banner_title,
                "links": self.graph_URLs
            },
            "requireauth": False,
            "auth": {
                "username": "Business Analytics",
                "passphrase": ""
            }
        }

        response = requests.post('https://dashboards.ly/publish',
                                 data={'dashboard': json.dumps(dashboard_json)},
                                 headers={'content-type': 'application/x-www-form-urlencoded'})
        response.raise_for_status()
        dashboard_url = response.json()['url']
        print('dashboard url: https://dashboards.ly{}'.format(dashboard_url))