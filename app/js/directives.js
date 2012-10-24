'use strict';

// D3 bar chart directive
// see http://docs.angularjs.org/guide/directive
angular.module('App.directives', [])
  .directive('glucoseDay', function () {
    return {
      restrict: 'E',
      terminal: true,
      scope: { val: '=' },
      link: function (scope, element, attrs) {
        // http://bl.ocks.org/3887118
        function getDate(d) { return new Date(d); }
        function getHour(d) {
          var x = new Date(d)
          return x.getHours();
        }

        var margin = {top: 20, right: 20, bottom: 30, left: 40},
            width = 960 - margin.left - margin.right,
            height = 500 - margin.top - margin.bottom;
        var x = d3.scale.linear().domain([0, 24]).range([0, width]).nice();
        var y = d3.scale.linear().range([height, 0]);
        var color = d3.scale.category10();
        var xAxis = d3.svg.axis().scale(x).orient("bottom");
        var yAxis = d3.svg.axis().scale(y).orient("left");

        var svg = d3.select("body").append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
          .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        // angular listener
        scope.$watch('val', function(newVal, oldVal) {
          if (!newVal) { return; }
          svg.selectAll('*').remove();

          // set the y domain after we have the data to auto scale
          y.domain([0, d3.max(newVal, function(d) { return d.value; })]).nice();

          svg.append("g")
              .attr("class", "x axis")
              .attr("transform", "translate(0," + height + ")")
              .call(xAxis)
            .append("text")
              .attr("class", "label")
              .attr("x", width)
              .attr("y", -6)
              .style("text-anchor", "end")
              .text("Time of day");

          svg.append("g")
                  .attr("class", "y axis")
                  .call(yAxis)
                .append("text")
                  .attr("class", "label")
                  .attr("transform", "rotate(-90)")
                  .attr("y", 6)
                  .attr("dy", ".71em")
                  .style("text-anchor", "end")
                  .text("Glucose (mmol/L)")

            svg.selectAll(".dot")
                .data(newVal)
              .enter().append("circle")
                .attr("class", "dot")
                .attr("r", 5)
                .attr("cx", function(d) { return x(getHour(d.when)); })
                .attr("cy", function(d) { return y(d.value); })
                .style("fill", function(d) { return color(); });
        });
      }
    }
  })
