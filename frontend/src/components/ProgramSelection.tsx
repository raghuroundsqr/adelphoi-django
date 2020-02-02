/** @jsx jsx */
import React from "react";
import { jsx } from "@emotion/core";
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
  backdrop
} from "./styles";
import * as Types from "../api/definitions";

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
  // const changeProgram = (e: React.ChangeEvent<HTMLInputElement>) => {
  //   const value = e.currentTarget.value;
  //   props.onProgramSelect(value);
  // };

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
        <h1 css={subHeading}>FM Prediction</h1>
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
              <h1 css={subHeading}>Program Selection</h1>
              <div
                css={fieldRow}
                style={{ flexWrap: "wrap", marginBottom: 16 }}
              >
                <div css={fieldBox}>
                  <input
                    type="radio"
                    onChange={handleChange}
                    checked={values.program_type === "ISM"}
                    id="ISM"
                    name="referred_program"
                    value="ISM"
                  />
                  <label htmlFor="ISM">ISM</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    checked={values.program_type === "ISF"}
                    onChange={handleChange}
                    id="ISF"
                    name="referred_program"
                    value="ISF"
                  />
                  <label htmlFor="ISF">ISF</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    checked={values.program_type === "MHFO"}
                    onChange={handleChange}
                    id="MHFO"
                    name="referred_program"
                    value="MHFO"
                  />
                  <label htmlFor="MHFO">MHFO</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    checked={values.program_type === "SUBAB"}
                    onChange={handleChange}
                    value="SUBAB"
                    name="referred_program"
                  />
                  <label htmlFor="SUBAB">SUBAB</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    checked={values.program_type === "Diagnostic"}
                    onChange={handleChange}
                    value="Diagnostic"
                    name="referred_program"
                  />
                  <label htmlFor="Diagnostic">Diagnostic</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    checked={values.program_type === "SEXOF-MH"}
                    onChange={handleChange}
                    value="SEXOF-MH"
                    name="referred_program"
                  />
                  <label htmlFor="SEXOF-MH">SEXOF-MH</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    checked={values.program_type === "SEXOF-Secure"}
                    onChange={handleChange}
                    value="SEXOF-Secure"
                    name="referred_program"
                  />
                  <label htmlFor="SEXOF-Secure">SEXOF-Secure</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    checked={values.program_type === "SEXOF"}
                    onChange={handleChange}
                    value="SEXOF"
                    name="referred_program"
                  />
                  <label htmlFor="SEXOF">SEXOF</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    checked={values.program_type === "Enhanced"}
                    onChange={handleChange}
                    value="Enhanced"
                    name="referred_program"
                  />
                  <label htmlFor="Enhanced">Enhanced</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    checked={values.program_type === "Secure-Male"}
                    onChange={handleChange}
                    value="Secure-Male"
                    name="referred_program"
                  />
                  <label htmlFor="Secure-Male">Secure-Male</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    checked={values.program_type === "Secure-Female"}
                    onChange={handleChange}
                    value="Secure-Female"
                    name="referred_program"
                  />
                  <label htmlFor="Secure-Female">Secure-Female</label>
                </div>
                <div css={fieldBox}>
                  <input
                    type="radio"
                    checked={values.program_type === "Independent-Living"}
                    onChange={handleChange}
                    value="Independent-Living"
                    name="referred_program"
                  />
                  <label htmlFor="Independent-Living">Independent Living</label>
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
