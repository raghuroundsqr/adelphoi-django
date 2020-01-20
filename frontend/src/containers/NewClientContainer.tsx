import React from "react";
import { connect } from "react-redux";
import { Switch, Route } from "react-router-dom";

import * as Types from "../api/definitions";
import { AppState } from "../redux-modules/root";
import { ContainerProps } from "./Container";
import * as client from "../redux-modules/client";
import PredictionFormStep1 from "../components/PredictionFormStep1";
import PredictionFormStep2 from "../components/PredictionFormStep2";
import ProgramSelection from "../components/ProgramSelection";

export interface NewClientContainerState {
  isLoading: boolean;
  error: string;
  hasError: boolean;
}

export interface NewClientContainerProp extends ContainerProps {
  saveClient: (client: Types.Client) => void;
  insertClient: (client: Types.Client) => void;
  submitPrediction: (client: Types.Client) => void;
  getLocations: (client_code: string, selected_program: string) => void;
  saveLocationAndProgram: (selected_location: string) => void;
}

export class NewClientContainer extends React.Component<
  NewClientContainerProp,
  NewClientContainerState
> {
  constructor(props: NewClientContainerProp) {
    super(props);
    this.state = this.getInitialState();
  }
  getInitialState() {
    return {
      isLoading: false,
      hasError: false,
      error: ""
    };
  }

  saveClientStep1 = (client: Types.Client) => {
    const { history } = this.props;
    console.log("save client step 1 called");
    this.props.saveClient(client);
    history.push("/new-client/2");
  };

  getLocations = async (selected_program: string) => {
    const { client: clientState } = this.props;
    if (!clientState || !clientState.client) {
      return false;
    }
    this.setState({ isLoading: true });
    console.log("getting location suggestions for selected program");
    await this.props.getLocations(
      clientState.client.client_code!,
      selected_program
    );
    this.setState({ isLoading: false });
    // history.push("/program-selection");
  };

  submitProgram = async (client: Types.Client) => {
    const { client: clientState } = this.props;
    if (!clientState || !clientState.client) {
      return false;
    }
    console.log("submit Prediction called");
    this.setState({ isLoading: true });
    await this.props.submitPrediction(client);
    this.setState({ isLoading: false });
    // history.push("/program-selection");
  };

  saveProgramAndLocation = async (selected_location: string) => {
    const { client: clientState } = this.props;
    if (!clientState || !clientState.client) {
      return false;
    }
    console.log("saveProgramAndLocation called");
    this.setState({ isLoading: true });
    await this.props.saveLocationAndProgram(selected_location);
    this.setState({ isLoading: false });
    // history.push("/program-selection");
  };

  saveClientStep2 = async (client: Types.Client) => {
    console.log("save client step 2 called");
    const { history } = this.props;
    try {
      this.setState({ isLoading: true });
      this.props.saveClient(client);
      await this.props.insertClient(client);
      this.setState({ isLoading: false });
      history.push("/new-client/program-selection");
    } catch (error) {
      console.log(error);
      this.setState({ isLoading: false });
    }
  };

  render() {
    const { client: clientState } = this.props;
    let currentClient: Types.Client;
    currentClient = clientState ? clientState.client : Types.emptyClient;

    return (
      <Switch>
        <Route exact path="/new-client/program-selection">
          <ProgramSelection
            client={currentClient}
            {...this.state}
            onProgramSelect={this.getLocations}
            onLocationSelect={this.saveProgramAndLocation}
            submitPrediction={this.submitProgram}
            isLoading={this.state.isLoading}
          />
        </Route>
        <Route exact path="/new-client/2">
          <PredictionFormStep2
            {...this.state}
            client={currentClient}
            onFormSubmit={this.saveClientStep2}
          />
        </Route>
        <Route exact path="/new-client">
          <PredictionFormStep1
            {...this.state}
            client={currentClient}
            onFormSubmit={this.saveClientStep1}
          />
        </Route>
      </Switch>
    );
  }
}

const mapStateToProps = (state: AppState) => {
  return {
    client: state.client
  };
};

const mapDispatchToProps = {
  saveClient: client.actions.upsertClient,
  insertClient: client.actions.insertClient,
  submitPrediction: client.actions.submitPrediction,
  getLocations: client.actions.getLocations,
  saveLocationAndProgram: client.actions.saveLocationAndProgram
};

export default connect(mapStateToProps, mapDispatchToProps)(NewClientContainer);
