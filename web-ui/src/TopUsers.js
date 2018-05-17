import React, { Component } from 'react';
import { VictoryTheme, VictoryTooltip,VictoryGroup, VictoryBar, VictoryAnimation, VictoryBrushLine, VictoryChart, VictoryLine, VictoryLabel, VictoryPie} from 'victory';

class TopUsers extends React.Component {

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
          domain={{ y: [0, 10] , x: [0, this.props.DataSet[0].y]}}
        >
            <VictoryGroup horizontal
              //height = {250}
              //offset={10}
              style={{ data: { width: 15 } }}
              colorScale={["green", "tomato"]}
            >
              <VictoryBar
                labelComponent={<VictoryTooltip/>}
                data={this.props.DataSet}
              />


          </VictoryGroup>
        </VictoryChart>
      </div>
    );
  }
}

export default TopUsers;