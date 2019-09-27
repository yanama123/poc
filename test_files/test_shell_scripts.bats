#!/usr/bin/env bats

@test "addition using bc" {
  result="$(echo 2+2 | bc)"
  [ "$result" -eq 4 ]
}
@test "addition using cd" {
  result="$(echo 2+4 | bc)"
  [ "$result" -eq 6 ]
}

@test "addition using ef" {
  result="$(echo 2 2+p | dc)"
  [ "$result" -eq 4 ]
}
