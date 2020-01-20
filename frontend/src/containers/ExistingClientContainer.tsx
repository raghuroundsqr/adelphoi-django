import React from "react";
import { connect } from "react-redux";
import { Switch, Route } from "react-router-dom";
import { AppState } from "../redux-modules/root";
import { ContainerProps } from "./Container";
import * as client from "../redux-modules/client";
import ClientSearch from "../components/ClientSearch";
import ClientDetails from "../components/ClientDetails";

export interface ExistingClientContainerState {
  isLoading: boolean;
  error: string;
  hasError: boolean;
  program_completion_response: string | null;
}

export interface ExistingClientContainerProp extends ContainerProps {
  searchClient: (client_code: string, client_name: string) => void;
  updateProgramCompletion: (
    client_code: string,
    program_completion: string,
    returned_to_care: string
  ) => Promise<string>;
}

export class ExistingClientContainer extends React.Component<
  ExistingClientContainerProp,
  ExistingClientContainerState
> {
  constructor(props: ExistingClientContainerProp) {
    super(props);
    this.state = this.getInitialState();
  }
  getInitialState() {
    return {
      isLoading: false,
      hasError: false,
      error: "",
      program_completion_response: null
    };
  }

  searchClient = async (client_code: string, client_name: string) => {
    // const { history } = this.props;
    await this.props.searchClient(client_code, client_name);
    // history.push("/new-client/2");
  };

  updateProgramCompletion = async (
    client_code: string,
    program_completion: string,
    returned_to_care: string
  ) => {
    this.setState({ isLoading: true });
    try {
      const response = await this.props.updateProgramCompletion(
        client_code,
        program_completion,
        returned_to_care
      );
      this.setState({
        isLoading: false,
        program_completion_response: response
      });
    } catch (error) {
      this.setState({ isLoading: false, program_completion_response: "error" });
    }
    // history.push("/new-client/2");
  };

  render() {
    const { client: clientState } = this.props;

    const clientList = (clientState && clientState.clientList) || [];
    return (
      <Switch>
        <Route exact path="/existing-client">
          <ClientSearch
            clientList={clientList}
            {...this.state}
            onFormSubmit={this.searchClient}
          />
        </Route>
        <Route exact path="/existing-client/client-details/:index">
          <ClientDetails
            clientList={clientList}
            {...this.state}
            onFormSubmit={this.updateProgramCompletion}
            program_completion_response={this.state.program_completion_response}
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
  searchClient: client.actions.searchClient,
  updateProgramCompletion: client.actions.updateProgramCompletion
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ExistingClientContainer);
