import * as Types from "../../api/definitions"; // CRA does not support abs paths for typescript yet.
import { FormikErrors } from "formik";
export interface ClientState {
  client: Types.Client;
  clientList: Types.Client[];
  errors: FormikErrors<Types.Client>;
  excludePage2: boolean;
  page1FormCompleted: boolean;
  page2FormCompleted: boolean;
}

export interface ConfigurationState {
  configuration: Types.Configuration;
}
export interface ProgramState {
  programList: Types.Program[];
}

export const emptyProgram: Types.Program = {
  program: "",
  program_name: ""
};
