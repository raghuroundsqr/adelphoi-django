import { combineReducers } from "redux";

import { clientReducer } from "./client";
import { configurationReducer } from "./configuration";

export const rootReducer = combineReducers({
  client: clientReducer,
  configuration: configurationReducer
});

export type AppState = ReturnType<typeof rootReducer>;
