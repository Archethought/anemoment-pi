describe("Graph", function () {
    var DATA_URL = 'data_source'
    var MOCK_DATA = 'mock_data'

    beforeEach(function () {
        this.graph = new Graph(DATA_URL);
        spyOn
    });

    describe("when it is initialized", function () {

        it("updates the data url", function() {
            expect(this.graph.data_url).toBe(DATA_URL)
        });

    });
/*
    describe("when it is rendered", function() {
       beforeEach(function () {
           this.graph = new Graph(DATA_URL);
           spyOn(this.graph, "renderC3");
           this.graph.render();
       });

       it("renders a C3 graph with no data", function () {
           expect(this.graph.renderC3).toHaveBeenCalled();
       });
    });
*/
});