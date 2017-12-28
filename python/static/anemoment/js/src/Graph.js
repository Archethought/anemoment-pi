/**
 * Represents a graph object
 * @param {string} data_url - The relative URL of the json-formatted graph data.
 * @constructor
 */
function Graph(data_url) {
    this.data_url = data_url;
    this.c3_graph = null;
}

/**
 * Renders the graph on the page
 */
Graph.prototype.render = function () {
    this.c3_graph = this.renderC3();
};

/**
 * Updates the graph with the data at data_url
 */
Graph.prototype.update = function () {
    this.updateC3(this.c3_graph, this.data_url);
};

/**
 * Generates the C3 graph and returns the associated object
 */
Graph.prototype.renderC3 = function () {
};

/**
 * Update the c3 graph
 * @param {c3 chart} graph - the c3 graph to update
 * @param {string} data_url - The relative URL of the json-formatted graph data.
 */
Graph.prototype.updateC3 = function (graph, data_url) {
};