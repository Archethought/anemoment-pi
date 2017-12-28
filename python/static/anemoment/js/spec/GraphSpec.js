describe("Graph", function () {
    var DATA_URL = 'data_source'
    var MOCK_C3_GRAPH = 'mock_data'

    beforeEach(function () {
        this.graph = new Graph(DATA_URL);
    });

    describe("when it is initialized", function () {
        it("updates the data url", function() {
            expect(this.graph.data_url).toBe(DATA_URL);
        });

        it("does not render the c3 graph", function() {
            expect(this.graph.c3_graph).toBe(null);
        });
    });

    describe("when it is rendered", function() {
        beforeEach(function () {
            spyOn(this.graph, 'renderC3').and.returnValue(MOCK_C3_GRAPH);
            this.graph.render();
        });

        it("renders a C3 graph", function () {
            expect(this.graph.renderC3).toHaveBeenCalled();
        });

        it("updates the c3_graph parameter", function () {
            expect(this.graph.c3_graph).toBe(MOCK_C3_GRAPH);
        });
    });

    describe("when it is updated", function () {
        beforeEach(function () {
            spyOn(this.graph, 'updateC3');
            this.graph.c3_graph = MOCK_C3_GRAPH;
            this.graph.update();
        });

        it("updates the stored c3_graph with data from the stored data_url", function () {
            expect(this.graph.updateC3).toHaveBeenCalledWith(MOCK_C3_GRAPH, DATA_URL);
        });
    });

});