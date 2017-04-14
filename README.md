# Building a Bokeh Dashboard Template for generic EDA

## Current features:

Two tabs intended:
1. Univariate visualization (Under construction)
2. Bivariate visualization (Yet to be constructed)

4 graphs exist, demonstrating each of the following functionalities:
1. Use of slider to change n, where y = x^n
2. Tap tool to select data points and fire a message box
3. Selection of points in one chart, auto-calculating summary stats in another

Additionally, following features exist:
1. Coordinated selection, panning and zooming
2. Hovertool on all charts to call out point-wise description
3. Dropdown to select a data-table with summary stats of the chosen variable

## Plans for future
The code is in a script format at the moment, and needs to be changed to a module in future versions.

The dashboard is also dependent on CSS and YAML files for styling, which needs to be included in as an argument in the package itself.

At the moment, the code should give an executable folder which can be run to demonstrate the dashboard in the browser. This may change in future versions.