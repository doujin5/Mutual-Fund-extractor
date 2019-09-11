var http = require("https");

var options = {
	"method": "GET",
	"hostname": "latest-mutual-fund-nav.p.rapidapi.com",
	"port": null,
	"path": "/fetchLatestNAV?MutualFundFamily=Sundaram%20Mutual%20Fund&SchemeType=All",
	"headers": {
		"x-rapidapi-host": "latest-mutual-fund-nav.p.rapidapi.com",
		"x-rapidapi-key": "07357d98a4mshf1716b2a4f26473p165059jsnd7d85d4ee227"
	}
};

var req = http.request(options, function (res) {
	var chunks = [];

	res.on("data", function (chunk) {
		chunks.push(chunk);
	});

	res.on("end", function () {
		var body = Buffer.concat(chunks);
		console.log(body.toString());
	});
});

req.end();