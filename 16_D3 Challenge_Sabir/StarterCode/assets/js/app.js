// set svg vars
var svgWidth = 800;
var svgHeight = 500;

var margin = {
    top: 20,
    right: 40,
    bottom: 60,
    left: 80
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3
    .select("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

// group charts
var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Import Data

d3.csv("assets/data/data.csv").then(function (povData) {

    // Step 1: Parse Data/Cast as numbers
    // ==============================
    povData.forEach(function (xdata) {
        xdata.poverty = +xdata.poverty;
        xdata.healthcare = +xdata.healthcare;

    });
    // Step 2: Create scale functions
    // x function
    var xLinearScale = d3.scaleLinear()
        .domain([d3.min(povData, d => d.poverty) * 0.9,
        d3.max(povData, d => d.poverty) * 1.1])
        .range([0, width]);

    // y function
    var yLinearScale = d3.scaleLinear()
        .domain([0, d3.max(povData, d => d.healthcare) * 1.1])
        .range([height, 0]);
    // Step 3: Create axis functions
    // set bottom/left axes
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);
    // Step 4: Append Axes to the chart
    // x axis
    chartGroup.append("g")
        .attr("transform", `translate(0, ${height})`)
        .style("font-size", "16px")
        .call(bottomAxis);

    // y axis
    chartGroup.append("g")
        .style("font-size", "16px")
        .call(leftAxis);

    // Step 5: Create Circles
    var circlesGroup = chartGroup.selectAll("circle")
        .data(povData)
        .enter()
        .append("circle")
        .attr("cx", d => xLinearScale(d.poverty))
        .attr("cy", d => yLinearScale(d.healthcare))
        .attr("r", 12)
        .attr("fill", "purple")
        .attr("opacity", "0.6");

    // Step 5: add State abbrev to circles
    let texts = svg.selectAll(null)
    chartGroup.selectAll("text.text-circles")
        .data(povData)
        .enter()
        .append("text")
        .classed("text-circles", true)
        .text(d => d.abbr)
        .attr("x", d => xLinearScale(d.poverty))
        .attr("y", d => yLinearScale(d.healthcare))
        .attr("dy", 5)
        .attr("text-anchor", "middle")
        .attr("font-size", "12px")
        .attr("fill", "white");

    // Step 6: Initialize tool tip
    // ==============================
    var toolTip = d3.tip()
        .attr("class", "tooltip")
        .offset([80, -60])
        .html(function (d) {
            return (`${d.state}</span><br>Poverty: ${d.poverty}%<br>Healthcare: ${d.healthcare}%`);
        });
    // Step 7: Create tooltip in the chart
    // ==============================
    chartGroup.call(toolTip);
    // Step 8: Create event listeners to display and hide the tooltip
    // ==============================
    circlesGroup.on("click", function (povdata) {
        toolTip.show(povdata, this);
    })
        // onmouseout event
        .on("mouseout", function (povdata, index) {
            toolTip.hide(povdata);
        });
    texts.on("click", function (data) {
        toolTip.show(povdata, this);
    })
        // onmouseout event
        .on("mouseout", function (povdata, index) {
            toolTip.hide(povdata);
        });


    //Step 9: Create axes labels
    // y axis
    chartGroup.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 30 - margin.left)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1em")
        .attr("class", "axisText")
        .text(" Healthcare (%)");

    // x axis
    chartGroup.append("text")
        .attr("y", height + margin.bottom / 2 - 10)
        .attr("x", width / 2)
        .attr("dy", "1em")
        .attr("class", "axisText")
        .text("Poverty Rate (%)");



});