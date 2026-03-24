/** @odoo-module */
import { CategorySelector } from "@point_of_sale/app/components/category_selector/category_selector";
import { patch } from "@web/core/utils/patch";
import { onMounted, useRef } from "@odoo/owl";

patch(CategorySelector.prototype, {
    setup() {
        super.setup(...arguments);
        this.customScrollRef = useRef("customScroll");
        
        onMounted(() => {
            const slider = this.customScrollRef.el;
            if (!slider) return;

            let isDown = false;
            let startX;
            let scrollLeft;
            let isDragging = false;

            slider.addEventListener('mousedown', (e) => {
                isDown = true;
                isDragging = false;
                startX = e.pageX - slider.offsetLeft;
                scrollLeft = slider.scrollLeft;
                slider.style.cursor = 'grabbing';
            });

            slider.addEventListener('mouseleave', () => {
                isDown = false;
                slider.style.cursor = '';
            });

            slider.addEventListener('mouseup', () => {
                isDown = false;
                slider.style.cursor = '';
                setTimeout(() => { isDragging = false; }, 50);
            });

            slider.addEventListener('mousemove', (e) => {
                if (!isDown) return;
                e.preventDefault();
                const x = e.pageX - slider.offsetLeft;
                const walk = (x - startX);
                if (Math.abs(walk) > 5) {
                    isDragging = true;
                }
                slider.scrollLeft = scrollLeft - walk;
            });

            // Capture phase click listener to prevent clicking items when dragging
            slider.addEventListener('click', (e) => {
                if (isDragging) {
                    e.preventDefault();
                    e.stopPropagation();
                }
            }, true); // true = capture phase
        });
    }
});
