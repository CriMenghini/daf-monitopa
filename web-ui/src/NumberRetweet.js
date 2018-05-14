import React, { Component } from 'react';
import { VictoryTheme, VictoryTooltip,VictoryGroup, VictoryBar, VictoryAnimation, VictoryBrushLine, VictoryChart, VictoryLine, VictoryLabel, VictoryPie} from 'victory';

class NumRetweet extends React.Component {
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
          domain={{ y: [0, 10] , x: [-10,10]}}
        >
            <VictoryGroup horizontal
              //height = {250}
              //offset={10}
              style={{ data: { width: 15 } }}
              colorScale={["green", "tomato"]}
            >
              <VictoryBar
                labelComponent={<VictoryTooltip/>}
                data={[
                  { x: 1, y: 1 , label: 'ciao'},
                  { x: 2, y: 2 ,label: 'ciao'},
                  { x: 3, y: 3 ,label: 'ciao'},
                  { x: 4, y: 4 ,label: 'ciao'},
                  { x: 5, y: 5 ,label: 'ciao'},
                  { x: 6, y: 6 ,label: 'ciao'},
                  { x: 7, y: 7 ,label: 'ciao'},
                  { x: 8, y: 8, label: 'ciao'},
                  { x: 9, y: 9 ,label: 'ciao'},
                  { x: 10, y: 10,label: 'ciao' }
                ]}
              />

              <VictoryBar
                labelComponent={<VictoryTooltip/>}
                data={[
                  { x: 1, y: -1 , label: 'ciao'},
                  { x: 2, y: -2 ,label: 'ciao'},
                  { x: 3, y: -3 ,label: 'ciao'},
                  { x: 4, y: -4 ,label: 'ciao'},
                  { x: 5, y: -5 ,label: 'ciao'},
                  { x: 6, y: -6 ,label: 'ciao'},
                  { x: 7, y: -7 ,label: 'ciao'},
                  { x: 8, y: -8, label: 'ciao'},
                  { x: 9, y: -9 ,label: 'ciao'},
                  { x: 10, y: -10,label: 'ciao' }
                ]}
              />
          </VictoryGroup>
        </VictoryChart>
      </div>
    );
  }
}

export default NumRetweet;