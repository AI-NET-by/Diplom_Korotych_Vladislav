from locust import HttpUser, SequentialTaskSet, task, between


class User(HttpUser):
    @task
    class SequenceOfTasks(SequentialTaskSet):

        # wait_time = between(1, 5)

        @task
        def mainPage(self):
            self.client.get("/")

        @task
        def ideasPage(self):
            self.client.get("/ideas/", verify=False)

        @task
        def AboutPage(self):
            self.client.get("/_/_/about/", verify=False)
        @task
        def BusinessPage(self):
            self.client.get("/_/_/business/", verify=False)

        @task
        def BlogPage(self):
            self.client.get("/_/_/blog/?utm_source=organicpins_pinsite_homepageicon&utm_campaign=pinterest_homepage_blogicon_all_evergreen&utm_medium=organic-pinterest", verify=False)
