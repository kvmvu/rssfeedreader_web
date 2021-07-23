var rssApp = new Vue({
    el: '#rss-app',

    data: {
        items: [],
        feeds: [],
        newLink: "",
        route: "feeds",
		showMessage: false
    },

    methods: {
		api: function(endpoint, method, data) {
			var config = {
				method: method || 'GET',
				body: data !== undefined ? JSON.stringify(data) : null,
				headers: {
					'content-type': 'application/json'
				}
			};

			return fetch(endpoint, config)
					.then((response) => response.json())
				// .then((data) => {
				// 	console.log(data)
				// })
					.catch((error) => console.log(error));
		},

        setup: function() {
		    var hash = window.location.hash;

		    if(hash) {
		        this.route = hash.slice(1);
            }
		    this.reload();
        },

		reload: function() {
			this.getItems();
			this.getFeeds();
		},

		getFeeds: function() {
			this.api("/feeds/").then((feeds) => {
				this.feeds = feeds;
			});
		},

		getItems: function() {
			this.api("/items/").then((items) => {
				this.items = items;
			});
		},

		newFeed: function() {
			this.api("/feeds/", "POST", { url: this.newLink }).then(() => {
				this.showMessage = true
				setTimeout(() => {
					this.showMessage = false
				}, 2000)

				this.reload()
				this.newLink = "";
			});
		},

		deleteFeed: function(id) {
			this.api("/feeds/" + id + "/", "DELETE").then(() => {
				this.reload();
			});
		},

		setRoute: function(route) {
            this.route = route;
        }
	}
});