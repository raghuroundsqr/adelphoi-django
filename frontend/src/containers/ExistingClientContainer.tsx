import React from "react";
import { connect } from "react-redux";
import { Switch, Route, RouteComponentProps } from "react-router-dom";
import { withSnackbar, WithSnackbarProps } from "notistack";
import { AppState } from "../redux-modules/root";
import * as program from "../redux-modules/program";
import { ContainerProps } from "./Container";
import * as client from "../redux-modules/client";
import ClientSearch from "../components/ClientSearch";
import ClientDetails from "../components/ClientDetails";

interface MatchParams {
  index: string;
}

interface MatchProps extends RouteComponentProps<MatchParams> {}

export interface ExistingClientContainerState {
  isLoading: boolean;
  error: string;
  hasError: boolean;
  program_completion_response: string | null;
}

export interface ExistingClientContainerProp
  extends ContainerProps,
    WithSnackbarProps {
  searchClient: (client_code: string, client_name: string) => void;
  updateProgramCompletion: (
    client_code: string,
    program_completion: number,
    returned_to_care: number
  ) => Promise<string>;
  getAvailablePrograms: () => Promise<void>;
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

  componentDidMount() {
    this.props.closeSnackbar();
    this.props.getAvailablePrograms();
  }

  searchClient = async (client_code: string, client_name: string) => {
    await this.props.searchClient(client_code, client_name);
  };

  updateProgramCompletion = async (
    client_code: string,
    program_completion: number,
    returned_to_care: number
  ) => {
    this.setState({ isLoading: true });
    try {
      const response = await this.props.updateProgramCompletion(
        client_code,
        program_completion,
        returned_to_care
      );
      this.setState({
        isLoading: false
        // program_completion_response: response
      });
      this.props.enqueueSnackbar("Data saved successfully.");
    } catch (error) {
      this.setState({
        isLoading: false
        // program_completion_response: "An error occured. Please try again."
      });
      this.props.enqueueSnackbar("An error occured. Please try again.");
    }
  };

  render() {
    const { client: clientState, program: programState } = this.props;

    const clientList = (clientState && clientState.clientList) || {};
    const availableProgramList =
      (programState && programState.availableProgramList) || [];

    return (
      <Switch>
        <Route exact path="/existing-client">
          <ClientSearch
            clientList={Object.values(clientList)}
            {...this.state}
            onFormSubmit={this.searchClient}
          />
        </Route>
        <Route
          exact
          path="/existing-client/client-details/:index"
          render={({ match }: MatchProps) => {
            const { index } = match.params;
            return (
              <ClientDetails
                client={clientList[index]}
                {...this.state}
                onFormSubmit={this.updateProgramCompletion}
                program_completion_response={
                  this.state.program_completion_response
                }
                programList={availableProgramList}
              />
            );
          }}
        ></Route>
      </Switch>
    );
  }
}

const mapStateToProps = (state: AppState) => {
  return {
    client: state.client,
    program: state.program
  };
};

const mapDispatchToProps = {
  searchClient: client.actions.searchClient,
  updateProgramCompletion: client.actions.updateProgramCompletion,
  getAvailablePrograms: program.actions.getAvailablePrograms
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(withSnackbar(ExistingClientContainer));
