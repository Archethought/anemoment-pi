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

            data.forEach(function (d) {
                d.timestamp = graph.parseTime(d.timestamp);
            });

            graph.c3_graph = c3.generate({
                bindto: bind_to,
                data: {
                    json: data,
                    keys: {
                        x: 'timestamp',
                        value: ['speed', 'direction', 'temperature'],
                    }
                },
                transition: {
                    duration: 0
                },
                tooltip: {
                    show: false
                },
                axis: {
                    x: {
                        type: 'timeseries',
                        tick: {
                            format: '%M:%S',
                            max: 2,
                            count: 20,
                        }
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
            data.forEach(function(d) {
                d.timestamp = parseTime(d.timestamp);
                if (d.timestamp > latest_time) {
                    latest_time = d.timestamp;
                }
            });

            var start_time = d3.time.minute.offset(latest_time, -1);
            chart.load({
                json: data,
                keys: {
                    x: 'timestamp',
                    value: ['speed', 'direction', 'temperature'],
                }
            });
            chart.axis.min({x: start_time});
            chart.axis.max({x: latest_time});
        });
    }
}
