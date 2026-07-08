export interface Rule {
  index: number;
  field: string;
  value: string;
  display: string
}

export interface Cell {
  symbol: string | null;
  player: string | null;
}

export interface GameResponse {
  game_id: string;
  board: Cell[][];
  current_turn: string;
  is_finished: boolean;
  winner: string | null;
  row_rules: Rule[];
  col_rules: Rule[];
  winning_line: number[][] | null;
}