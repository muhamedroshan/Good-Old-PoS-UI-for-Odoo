
/** @odoo-module */

import { ProductCard } from "@point_of_sale/app/components/product_card/product_card";
import { patch } from "@web/core/utils/patch";
import { usePos } from "@point_of_sale/app/hooks/pos_hook";

patch(ProductCard.prototype, {
    setup() {
        super.setup();
        this.pos = usePos();
    },
    get price() {
        if (!this.props.product) {
            return ""
        }
        return this.env.utils.formatCurrency(this.props.product.list_price)
    }
});
