import { combineReducers } from "redux";

import { clientReducer } from "./client";
import { programReducer } from "./program";

export const rootReducer = combineReducers({
  client: clientReducer,
  program: programReducer
});

export type AppState = ReturnType<typeof rootReducer>;
