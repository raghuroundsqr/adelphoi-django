import React from "react";
import { connect } from "react-redux";
import { Switch, Route, Link } from "react-router-dom";
import { withSnackbar, WithSnackbarProps } from "notistack";
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

export interface NewClientContainerProp
  extends ContainerProps,
    WithSnackbarProps {
  saveClient: (
    client: Types.Client,
    page1FormCompleted?: boolean,
    excludePage2?: boolean
  ) => void;
  insertClient: (client: Types.Client) => void;
  submitPrediction: (client: Types.Client) => void;
  getLocations: (client_code: string, selected_program: string) => void;
  saveLocationAndProgram: (selected_location: string) => void;
  clearErrors: () => void;
  clearClient: () => void;
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

  saveClientStep1 = async (client: Types.Client) => {
    const { history } = this.props;
    this.props.clearErrors();
    // check excl criteria
    if (client.Exclusionary_Criteria) {
      // return this.saveClientStep2(client);
      try {
        this.setState({ isLoading: true });
        this.props.saveClient(client, true, true);
        await this.props.insertClient(client);
        this.setState({ isLoading: false });
        this.props.enqueueSnackbar("Data saved successfully.");
        this.props.clearErrors();
      } catch (error) {
        console.log(error);
        this.setState({ isLoading: false });
      }
    } else {
      this.props.saveClient(client, true, false);
      history.push("/new-client/2");
    }
  };

  getLocations = async (selected_program: string) => {
    const { client: clientState } = this.props;
    if (!clientState || !clientState.client) {
      return false;
    }
    this.setState({ isLoading: true });
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
    this.props.enqueueSnackbar("Data saved successfully.");
  };

  saveClientStep2 = async (client: Types.Client) => {
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
      this.props.enqueueSnackbar("An error occurred." + error);
    }
  };

  render() {
    const { client: clientState } = this.props;
    let currentClient: Types.Client;
    // let currentErrors: Partial<Types.Client> | undefined;
    currentClient = clientState ? clientState.client : Types.emptyClient;
    // currentErrors = clientState ? clientState.errors : undefined;

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
        <Route
          exact
          path="/new-client/2"
          render={routeProps => {
            console.log("form 1 completed ");
            const step1 = clientState
              ? clientState.page1FormCompleted
              : this.state.isLoading;
            console.log("form 1 completed ", step1);
            if (!step1) {
              return (
                <h1>
                  Error. First step of the new client form is incomplete.
                  <Link to="/new-client">Click here to begin.</Link>
                </h1>
              );
            }
            return (
              <PredictionFormStep2
                {...this.state}
                {...routeProps}
                client={currentClient}
                onFormSubmit={this.saveClientStep2}
                errors={(clientState && clientState.errors) || undefined}
              />
            );
          }}
        ></Route>
        <Route exact path="/new-client">
          <PredictionFormStep1
            {...this.state}
            client={currentClient}
            onFormSubmit={this.saveClientStep1}
            errors={(clientState && clientState.errors) || undefined}
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
  saveLocationAndProgram: client.actions.saveLocationAndProgram,
  clearErrors: client.actions.clearErrors,
  clearClient: client.actions.clear
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(withSnackbar(NewClientContainer));
