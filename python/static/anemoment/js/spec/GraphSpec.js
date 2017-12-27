describe("Graph", function () {
    var DATA_URL = 'data_source'

    beforeEach(function () {
        this.graph = new Graph();
    });

    it("can be initialized with a data source", function() {
        this.graph.init(DATA_URL)
        expect(this.graph.data_source).toBe(DATA_URL)
    });
});