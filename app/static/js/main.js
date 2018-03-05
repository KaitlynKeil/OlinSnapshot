var data_sample = 
{
  "data": [
    {
      "name": "Food",
      "children": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        },
        {        
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        }
      ]
    },
    {
      "name":"Event",
      "children": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        },
        {        
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        }

      ]
    },
    {
      "name":"Other",
      "children": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        },
        {        
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        }

      ]
    },
    {
      "name":"Lost",
      "children": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        },
        {       
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        }

      ]
    }
  ]
};

//var data_sample_json = JSON.parse(data_sample);

var example_2 =
{
  "name": "Data Development",
  "value": 60,
  "children": [
    {
      "name": "Data Visualization",
      "value": 40,
      "children": [
        {"name": "D3.js", "value": 10},
        {"name": "Dimple.js", "value": 9},
        {"name": "matplotlib(python)", "value": 8},
        {"name": "ggplot(R)", "value": 7}
      ]
    }, 
    {
      "name": "Data Analysis",
      "value": 20,
      "children": [
        {"name": "numpy", "value": 9},
        {"name": "scikit-learn", "value": 8}
      ]
    }
  ]
};

var test_json = {
  "name": "Food",
  "value": 60,
  "children": [
    {
      "event_time": "17:22:57",
      "body": "I am putting a Party",
      "event_place": "Boston Commons",
      "name": "Boston Tea Party",
      "event_data": "2018-03-02",
      "value": 5,
      "who": "kaitlyn"
    },
    {        
      "event_time": "17:22:57",
      "body": "I am putting a Party",
      "event_place": "Boston Commons",
      "name": "Boston Tea Party",
      "event_data": "2018-03-02",
      "value": 5,
      "who": "kaitlyn"
    }
  ]
};

var working_json = {
  "name": "Data Development",
  "value": 60,
  "children": [
    {
      "event_time": "17:22:57",
      "body": "I am putting a Party",
      "event_place": "Boston Commons",
      "name": "Boston Tea Party",
      "event_data": "2018-03-02",
      "value": 5,
      "who": "kaitlyn"
    },
    {        
      "event_time": "17:22:57",
      "body": "I am putting a Party",
      "event_place": "Boston Commons",
      "name": "Boston Tea Party",
      "event_data": "2018-03-02",
      "value": 5,
      "who": "kaitlyn"
    }
  ]
};

var working_json_v2 = 
{
  "name": "Data",
  "value": 60,
  "children": [
    {
      "name": "Food",
      "value": 60,
      "children": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        },
        {        
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        }
      ]
    },
    {
      "name": "Events",
      "value": 60,
      "children": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        },
        {        
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        }
      ]
    },
    {
      "name": "Other",
      "value": 60,
      "children": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        },
        {        
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        }
      ]
    },
    {
      "name": "Lost",
      "value": 60,
      "children": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        },
        {        
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        }
      ]
    }
  ]
};

var working_json_v3 = 
{
  "name": "Data",
  "value": 60,
  "children": [
    {
      "name": "Food",
      "value": 60,
      "children": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        },
        {        
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        }
      ]
    },
    {
      "name": "Events",
      "value": 60,
      "children": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        },
        {        
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        }
      ]
    },
    {
      "name": "Other",
      "value": 60,
      "children": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        },
        {        
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        }
      ]
    },
    {
      "name": "Lost",
      "value": 60,
      "children": [
        {
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        },
        {        
          "event_time": "17:22:57",
          "body": "I am putting a Party",
          "event_place": "Boston Commons",
          "name": "Boston Tea Party",
          "event_data": "2018-03-02",
          "value": 5,
          "who": "kaitlyn"
        }
      ]
    }
  ]
};

var categories = 
{
  "name": "Categories",
  "value": 60,
  "children": [
    {
      "name":  "Food",
      "value": data_sample.data[0].children.length * 5,
      "color": "green"
    },
    {
      "name":  "Other",
      "value": data_sample.data[1].children.length * 5,
      "color": "purple"
    },
    {
      "name":  "Lost",
      "value": data_sample.data[2].children.length * 5,
      "color": "red"
    },
    {
      "name":  "Events",
      "value": data_sample.data[3].children.length * 5,
      "color": "blue"
    }
  ]
};

var categories_2 = 
{
  "name": "Data Development",
  "value": 60,
  "children": [
    {"name": "D3.js", "value": 10},
    {"name": "Dimple.js", "value": 8},
    {"name": "matplotlib(python)", "value": 6},
    {"name": "ggplot(R)", "value": 4},
    {"name": "numpy", "value": 9},
    {"name": "scikit-learn", "value": 8}
  ]
}
console.log(data_sample.data[0].children.length * 5);
console.log(data_sample.data[1].children.length * 4);
console.log(data_sample.data[2].children.length * 3);
console.log(data_sample.data[3].children.length * 2);
console.log(categories);



//set screen pixel sizes
var width = 800, height = 600;

var chart = d3.select("body").append("svg")
  .attr("width", width).attr("height", height) 
  .append("g")
    .attr("transform", "translate(50,50)");

var pack = d3.layout.pack()
  .size([width, height - 50])
  .padding(10);

var nodes = pack.nodes(categories);

var node = chart.selectAll(".node")
    .data(nodes).enter()
  .append("g")
    .attr("class", "node")
    .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

node.append("circle")
    .attr("r",function(d) { return d.r })
    .attr("fill", function(d){ return d.children ? "#fff" : d.color; }) //make nodes with children invisible
    .attr("opacity", 0.25)
    .attr("stroke", function(d) { return d.children ? "#fff":"#ADADAD"; } ) //make nodes with children invisible
    .attr("stroke-width", 2);


node.append("text")
    .text(function(d) { return d.children ? "" : d.name; });



/*
// On Click, we want to go to next webpage for more information
svg.on("click", function() {
    var coords = d3.mouse(this);
    dataset.push(newData);   // Push data to our array

    svg.selectAll("circle")  // For new circle, go through the update process
      .data(dataset)
      .enter()
      .append("circle")
      .attr(circleAttrs)  // Get attributes from circleAttrs var
      .on("mouseover", handleMouseOver)
      .on("mouseout", handleMouseOut);
  })

// Create Event Handlers for mouse
function handleMouseOver(d, i) {  // Add interactivity

      // Use D3 to select element, change color and size
      d3.select(this).attr({
        fill: "orange",
        r: radius * 2
      });

      // Specify where to put label of text
      svg.append("text").attr({
         id: "t" + d.x + "-" + d.y + "-" + i,  // Create an id for text so we can select it later for removing on mouseout
          x: function() { return xScale(d.x) - 30; },
          y: function() { return yScale(d.y) - 15; }
      })
      .text(function() {
        return [d.x, d.y];  // Value of the text
      });
    }*/

/*function handleMouseOut(d, i) {
      // Use D3 to select element, change color back to normal
      d3.select(this).attr({
        fill: "black",
        r: radius
      });

      // Select text by id and then remove
      d3.select("#t" + d.x + "-" + d.y + "-" + i).remove();  // Remove text location
    }
*/


////////// PART 2 //////////

//set screen pixel sizes
var width = 800, height = 600;

var chart = d3.select("body").append("svg")
  .attr("width", width).attr("height", height) 
  .append("g")
    .attr("transform", "translate(50,50)");

var pack = d3.layout.pack()
  .size([width, height - 50])
  .padding(10);

d3.json("/data", function(error,quotes) {
  var nodes = pack.nodes(quotes.data[0]);

  var node = chart.selectAll(".node")
      .data(nodes).enter()
    .append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

  node.append("circle")
      .attr("r",function(d) { return d.r })
      .attr("fill", function(d){ return d.children ? "#fff" : "steelblue"; }) //make nodes with children invisible
      .attr("opacity", 0.25)
      .attr("stroke", function(d) { return d.children ? "#fff":"#ADADAD"; } ) //make nodes with children invisible
      .attr("stroke-width", 2);


  node.append("text")
      .text(function(d) { return d.children ? "" : d.name; });

});



var width = 800, height = 600;

var chart = d3.select("body").append("svg")
  .attr("width", width).attr("height", height)
  .append("g")
    .attr("transform", "translate(50,50)");

var pack = d3.layout.pack()
  .size([width, height - 50])
  .padding(10);


var nodes = pack.nodes(working_json_v2);

var node = chart.selectAll(".node")
    .data(nodes).enter()
  .append("g")
    .attr("class", "node")
    .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

node.append("circle")
    .attr("r",function(d) { return d.r; })
    .attr("fill", "steelblue")
    .attr("opacity", 0.25)
    .attr("stroke", "#ADADAD")
    .attr("stroke-width", 2);

node.append("text")
    .text(function(d) { return d.children ? "" : d.name; });






/*var width = 800, height = 600;

var chart = d3.select("body").append("svg")
  .attr("width", width).attr("height", height) 
  .append("g")
    .attr("transform", "translate(50,50)");

var pack = d3.layout.pack()
  .size([width, height - 50])
  .padding(10);

var nodes = pack.nodes(working_json_v2);

var node = chart.selectAll(".node")
    .data(nodes).enter()
  .append("g")
    .attr("class", "node")
    .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

node.append("circle")
    .attr("r",function(d) { return d.r })
    .attr("fill", function(d){ return d.children ? "#fff" : "steelblue"; }) //make nodes with children invisible
    .attr("opacity", 0.25)
    .attr("stroke", function(d) { return d.children ? "#fff":"#ADADAD"; } ) //make nodes with children invisible
    .attr("stroke-width", 2);


node.append("text")
    .text(function(d) { return d.children ? "" : d.name; });*/


