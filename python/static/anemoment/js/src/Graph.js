/**
 * Represents a graph object
 * @param {string} data_url - The relative URL of the json-formatted graph data.
 * @constructor
 */
class Graph {
    constructor (data_url) {
        this.data_url = data_url;
        this.c3_graph = null;
        this.bind_to = null;
    }

    parseTime (time) {
        if (time.includes(".")) {
            return d3.time.format("%Y-%m-%dT%H:%M:%S.%LZ").parse(time);
        } else {
            return d3.time.format("%Y-%m-%dT%H:%M:%SZ").parse(time);
        }
    }

    /**
    * Renders the graph on the page
    */
    render (bind_to) {
        this.bind_to = bind_to;
        this.c3_graph = this.renderC3(bind_to);
    }

    /**
     * Updates the graph with the data at data_url
     */
    update () {
        this.updateC3();
    }

    renderC3 (bind_to) {
        this.bind_to = bind_to;
        var graph = this;
        d3.json(this.data_url, function(error, data) {
            if (error) throw error;

            graph.c3_graph = c3.generate({
                bindto: bind_to,
                data: {
                    json: data,
                    keys: {
                        x: 'id',
                        value: ['speed', 'temperature'],
                    }
                },
                transition: {
                    duration: 0
                },
		interaction: {
		    enabled: false
		},
                tooltip: {
                    show: false
                },
		point: {
		    show: false
		},
		axis: {
		    y: {
		        tick: {
			    format: function(x) { return Math.round(x * 100) / 100; }
			}
		    },
		    x: {
			show: false
		    }
		}
            });
        });

    }

    updateC3() {
        var chart = this.c3_graph;
        var parseTime = this.parseTime;
        if (chart === undefined){
            return;
        }
        d3.json(this.data_url, function (error, data) {
            if (error) throw error;
            var latest_time = 0;

            chart.load({
                json: data,
                keys: {
                    x: 'id',
                    value: ['speed', 'temperature'],
                }
            });
        });
    }
}
