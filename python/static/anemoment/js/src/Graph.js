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
 * Generates the C3 graph and returns the associated object
 */
Graph.prototype.renderC3 = function () {

};