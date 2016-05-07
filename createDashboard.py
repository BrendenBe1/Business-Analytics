import requests, json

class createDashboard:
    """
    Combines graphs from Plotly API into a single webpage using Dashboardly
    """

    def __init__(self, graph_URLs, date_range):
        """
        Generate needed data and create dashboard

        :param graph_URLs: list of strings
        :param date_range: list of two strings
        :return: string of URL
        """

        self.date_range = date_range
        self.graph_URLs = graph_URLs

        # Reformat URLs into a list of dictionaries for the API
        self.rows_list = []
        for URL in graph_URLs:
            self.rows_list.append([{"plot_url" : URL}])

        self.banner_title = ""
        self.create_banner()
        self.generate()


    # Convert "date" to "date (time_type)"
    def create_banner(self):
        """
        Combine two dates into a single string

        :return: string
        """

        self.banner_title += self.date_range[0]
        self.banner_title += " to "
        self.banner_title += self.date_range[1]


    def generate(self):
        """
        Calls API to generate a link to the dashboard

        :return: string
        """

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
        print('Dashboard URL: https://dashboards.ly{}'.format(dashboard_url))