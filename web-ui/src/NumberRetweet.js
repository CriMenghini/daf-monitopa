import React, { Component } from 'react';
import { VictoryTheme, VictoryTooltip,VictoryGroup, VictoryBar, VictoryAnimation, VictoryBrushLine, VictoryChart, VictoryLine, VictoryLabel, VictoryPie} from 'victory';

class NumRetweet extends React.Component {

  componentDidMount() {

  }


  render() {
    return (
      <div>
        <VictoryChart
          height = {350}
          theme={VictoryTheme.grayscale}
          animate={{
                      duration: 2000,
                      onLoad: { duration: 1000 }
                    }}
          domain={{ y: [0, 10] , x: [-10, 10]}}
        >
            <VictoryGroup horizontal
              //height = {250}
              //offset={10}
              style={{ data: { width: 15 } }}
              colorScale={["green", "tomato"]}
            >
              <VictoryBar
                labelComponent={<VictoryTooltip/>}
                data={this.props.dati}
              />


          </VictoryGroup>
        </VictoryChart>
      </div>
    );
  }
}

export default NumRetweet;