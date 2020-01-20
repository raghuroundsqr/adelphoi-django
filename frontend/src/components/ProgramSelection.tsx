/** @jsx jsx */
import React from "react";
import { jsx, css } from "@emotion/core";
// import { useHistory } from "react-router-dom";
import { Formik, ErrorMessage } from "formik";
import Button from "@material-ui/core/Button";
import Backdrop from "@material-ui/core/Backdrop";
import CircularProgress from "@material-ui/core/CircularProgress";
import {
  wrap,
  subHeading,
  fieldRow,
  selectField,
  mainContent,
  twoCol,
  inputField,
  label,
  fieldBox,
  heading
} from "./styles";
import * as Types from "../api/definitions";

const backdrop = css`
  z-index: 5 !important;
  color: #fff;
`;

interface ProgramSelectionProps {
  client: Types.Client;
  onProgramSelect: (selected_program: string) => void;
  onLocationSelect: (selected_location: string) => void;
  submitPrediction: (client: Types.Client) => void;
  isLoading: boolean;
  hasError: boolean;
  error: string;
}

const ProgramSelection: React.FC<ProgramSelectionProps> = props => {
  const changeProgram = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.currentTarget.value;
    props.onProgramSelect(value);
  };

  const onLocationChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const value = e.currentTarget.value;
    props.onLocationSelect(value);
  };

  // const history = useHistory();
  /** */
  return (
    <div css={wrap}>
      <div css={mainContent}>
        <Backdrop css={backdrop} open={props.isLoading}>
          <CircularProgress color="inherit" />
        </Backdrop>

        <h1 css={heading}>Program Selection</h1>
        <Formik
          initialValues={props.client}
          enableReinitialize
          // validationSchema={Step2ValidationSchema}
          onSubmit={async (values, helpers) => {
            console.log(values);
            // add values to client state
            await props.submitPrediction(values);
            // helpers.resetForm();
          }}
        >
          {({
            values,
            handleSubmit,
            handleChange,
            handleBlur,
            touched,
            errors
          }) => (
            <form name="submitPredictionForm" onSubmit={handleSubmit}>
              <h1 css={subHeading}>Predictions</h1>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Program</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="Program"
                    css={inputField}
                    placeholder=""
                    value={values.program_type || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="Program" />
                </div>
              </div>

              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>% Match</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="Confidence"
                    css={inputField}
                    placeholder=""
                    value={values.Confidence || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="Confidence" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={label}>Level of care</label>
                </div>
                <div css={twoCol}>
                  <input
                    type="text"
                    name="Level_of_care"
                    css={inputField}
                    placeholder=""
                    value={values.Level_of_care || ""}
                    onChange={handleChange}
                  />
                  <ErrorMessage component="span" name="Level_of_care" />
                </div>
              </div>
              <div css={fieldRow} style={{ justifyContent: "flex-end" }}>
                <Button
                  type="submit"
                  size="large"
                  variant="contained"
                  color="primary"
                >
                  Submit
                </Button>
              </div>
            </form>
          )}
        </Formik>
        <h1 css={subHeading}>Result</h1>
        {props.client.model_program && (
          <div css={fieldRow}>
            <div css={fieldBox}>
              <input
                type="radio"
                id="referred_program"
                onChange={changeProgram}
                name="program_radio"
                value={props.client.referred_program || ""}
              />
              <label htmlFor="referred_program">
                {props.client.referred_program}
              </label>
            </div>
            <div css={fieldBox}>
              <input
                type="radio"
                id="model_program"
                onChange={changeProgram}
                name="program_radio"
                value={props.client.model_program || ""}
              />
              <label htmlFor="model_program">
                {props.client.model_program}
              </label>
            </div>
          </div>
        )}
        {props.client.SuggestedLocations &&
          props.client.SuggestedLocations.length > 0 && (
            <React.Fragment>
              <h1 css={subHeading}>Select Location</h1>
              <div css={fieldRow}>
                <select
                  css={selectField}
                  name="client_selected_location"
                  value={props.client.client_selected_locations || ""}
                  onChange={onLocationChange}
                >
                  <option value="">Select</option>
                  {props.client.SuggestedLocations.map(loc => (
                    <option key={loc} value={loc}>
                      {loc}
                    </option>
                  ))}
                </select>
              </div>
            </React.Fragment>
          )}
        {props.client.result_final && (
          <h1 css={subHeading}>{props.client.result_final}</h1>
        )}
      </div>
      {/* MAIN CONTENT */}
    </div>
  );
};

export default ProgramSelection;
