import React, { Component } from 'react';
import { Stage, Layer, Rect, Text } from 'react-konva';
import Konva from 'konva';


class Controller extends Component {

  render() {
    return (
      <Stage
          x={0}
          y={0}
          width={window.innerWidth}
          height={500}
          onMouseDown={this.handleClick}
        >
          <Layer>
            <Rect
              x = {10}
              y = {10}
              width={80}
              height={400}
              stroke={'black'}
              strokeWidth={2}

            />
            <Text
              x = {20}
              y = {20}
              text = {'Controll Bar'}
              align = {'center'}
              verticalAlign = {'middle'}
              fontSize = {10}
            />

          </Layer>
        </Stage>
    );
  }
}

export default Controller;