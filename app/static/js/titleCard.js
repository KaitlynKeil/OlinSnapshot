var data_sample = 
{
  "data": [
    {
      "category": "Food",
      "emails": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "subject": "Boston Tea Party",
          "event_data": "2018-03-02",
          "msg-id": 5,
          "who": "kaitlyn"
        },
        {        
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "subject": "Boston Tea Party",
          "event_data": "2018-03-02",
          "msg-id": 5,
          "who": "kaitlyn"
        }
      ]
    },
    {
      "category":"Event",
      "emails": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "subject": "Boston Tea Party",
          "event_data": "2018-03-02",
          "msg-id": 5,
          "who": "kaitlyn"
        },
        {        
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "subject": "Boston Tea Party",
          "event_data": "2018-03-02",
          "msg-id": 5,
          "who": "kaitlyn"
        }

      ]
    },
    {
      "category":"Other",
      "emails": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "subject": "Boston Tea Party",
          "event_data": "2018-03-02",
          "msg-id": 5,
          "who": "kaitlyn"
        },
        {        
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "subject": "Boston Tea Party",
          "event_data": "2018-03-02",
          "msg-id": 5,
          "who": "kaitlyn"
        }

      ]
    },
    {
      "category":"Lost",
      "emails": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "subject": "Boston Tea Party",
          "event_data": "2018-03-02",
          "msg-id": 5,
          "who": "kaitlyn"
        },
        {       
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "subject": "Boston Tea Party",
          "event_data": "2018-03-02",
          "msg-id": 5,
          "who": "kaitlyn"
        }

      ]
    }
  ]
};

//Create the SVG body
var svg = d3.select("body")
    .append("svg")
    .attr("width", '800px')
    .attr("height", '800px');

//Create all the circle objects based on the data
svg.selectAll("circle")
    .data([32, 57, 112, 293]) //bind data
  .enter().append("circle") //create circles 
    .attr("cy", 60) //y axis
    .attr("cx", function(d, i) { return i * 100 + 30; }) //x axis
    .attr("r", function(d) { return Math.sqrt(d); }); //radius

//create an empty tool top
var tooltip = d3.select("body")
  .append ("div")
  .style("position", "absolute")
  .style("z-index", "10")
  .style("visibility", "hidden")
  .style("color", "white")
  .style("padding", "8px")
  .style("background-color", "rgba(0, 0, 0, 0.75)")
  .style("border-radius", "6px")
  .style("font", "12px sans-serif")
  .text("tooltip");
//
/*
createGraph();

function createGraph() {*/
    var width = 960; // chart width
    var height = 700; // chart height
    var format = d3.format(",d");  // convert value to integer
    //v3 syntax
    var color = d3.scale.category20();  // create ordinal scale with 20 colors
    var sizeOfRadius = d3.scale.pow().domain([-100,100]).range([-50,50]);  // https://github.com/mbostock/d3/wiki/Quantitative-Scales#pow

    //create bubble in a specific layout format
    var bubble = d3.layout.pack()
        .sort(null)  // disable sorting, use DOM tree traversal
        .size([width, height])  // chart layout size
        .padding(1)  // padding between circles
        .radius(function(d) { return 20 }) //;+ (sizeOfRadius(d.data.category.emails.length) * 30); });  // radius for each circle

    //initialize SVG Body/chart
    var svg = d3.select('#chart').append('svg') //add the bubbles to all charts
        .attr('width',width)
        .attr('height',height)
        .attr('class', 'bubble');

    // REQUEST the Data from data index created in __init__.py
    d3.json("/data", function(error, quotes) {
      //create a node for each bubble file
      var node = svg.selectAll('.node')
      //bind data
        .data(bubble.nodes(quotes)
        .filter(function(d) { return !d.children; }))
        .enter().append('g')
        .attr('class', 'node')
        .attr('transform', function(d) { return 'translate(' + d.x + ',' + d.y + ')'});
      //add attributes to each create bubble
      node.append('circle')
        .attr('r', function(d) { return d.r; })
        .style('fill', function(d) { return color(d.symbol); });
      //add labeled text on top of each bubble
      node.append('text')
        .attr("dy", ".3em")
        .style('text-anchor', 'middle')
        .text(function(d) { return d.symbol; });

    })

    
    node.append("circle")
      .attr("r",function(d) { return d.data.category.emails.length; })
      .attr("fill", color) //make nodes with children invisible
      .attr("opacity", 0.25)
      .attr("stroke", color) //make nodes with children invisible
      .attr("stroke-width", 2);

    
    node.append("text")
      .text(function(d) { return d.name; });


    
    //Load data, issue with referencing data.json while in local http server
/*    d3.json("/data/data.json", function(data) {
      //create data object
      var nodes = bubble.nodes(data_sample);
      
      //create a node for each bubble file
      var node = chart.selectAll(".node")
          //bind data 
          .data(nodes).enter()
        .append("g")
          .attr("class", "node")
          .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

      //add attributes to each create bubble
      node.append("circle")
          .attr("r",function(d) { return d.r; })
          .attr("fill", function(d){ return d.children ? "#fff" : "steelblue"; }) //make nodes with children invisible
          .attr("opacity", 0.25)
          .attr("stroke", function(d) { return d.children ? "#fff":"#ADADAD"; } ) //make nodes with children invisible
          .attr("stroke-width", 2);

      //add labeled text on top of each bubble
      node.append("text")
          .text(function(d) { return d.name; });
    });*/


//}

