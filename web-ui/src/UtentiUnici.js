import React, { Component } from 'react';
import { VictoryArea, VictoryTheme, VictoryStack, VictoryBar, VictoryAnimation, VictoryBrushLine, VictoryChart, VictoryLine, VictoryLabel, VictoryPie} from 'victory';
//import { _ } from "jquery";
var _ = require('lodash');


class UtentiUnici extends React.Component {
  constructor(props) {
    super(props);
    this.state = {  dati: this.getData(),
                    recData: [this.props.unique]};
  }

  componentDidMount() {
    this.setStateInterval = window.setInterval(() => {
      this.setState({ dati: this.getData() });
    }, 4000);
    this.myStopFunction()
  }


   myStopFunction() {
    window.clearInterval(this.setStateInterval);
  }

  getData() {
    return _.range(1).map(() => {
      return this.props.unique;
    });
  }

  componentWillReceiveProps(nextProps){
	if(nextProps.unique){
		this.setState({
		    dati: [nextProps.unique],
			recData: [nextProps.unique]
		})
	}
}

  parseDate(date) {
        var arrayDate = new Array();

        for (var i=0; i < date.length; i++){
            var dict = {a: new Date(date[i].a), b: date[i].b}
            arrayDate.push(dict)
        }
        return arrayDate
  }

  render() {

    return (
      <VictoryChart
        scale={{ x: "time" }}
        theme={VictoryTheme.greyscale}
        animate={{ duration: 1000 }}
      >
        <VictoryStack
          colorScale={"blue"}
        >
          {this.state.dati.map((data, i) => {
            return (
              <VictoryArea
                key={i}
                data={data}
                interpolation={"basis"}
              />
            );
          })}
        </VictoryStack>
      </VictoryChart>
    );
  }
}

export default UtentiUnici;

