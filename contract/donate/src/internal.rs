use near_sdk::Promise;

use crate::*;

pub(crate) fn ntoy(near_amount: Balance) -> Balance {
    near_amount * 10u128.pow(24)
}

pub(crate) fn yton(yocto_amount: Balance) -> Balance {
    (yocto_amount + (5 * 10u128.pow(23))) / 10u128.pow(24)
}

pub(crate) fn random_number(num_of_voters: u64) -> u64 {
    env::block_timestamp() % num_of_voters
}

impl Donap {
    pub(crate) fn internal_transfer(
        &mut self,
        streamer_id: AccountId,
        amount: Balance,
        lucky_voter: AccountId,
    ) {
        let amount_of_streamer = amount * 95 / 100;
        let amount_of_voter = amount - amount_of_streamer;

        Promise::new(streamer_id)
            .transfer(amount_of_streamer)
            .and(Promise::new(lucky_voter).transfer(amount_of_voter));
    }
}
