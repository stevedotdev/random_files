document.addEventListener("DOMContentLoaded", function () {
  // Fictitious data
  const data = {
    totalSales: 25000,
    totalOrders: 1200,
    averageOrderValue: 150,
    topProducts: [
      { name: "Product A", img: "https://via.placeholder.com/50" },
      { name: "Product B", img: "https://via.placeholder.com/50" },
      { name: "Product C", img: "https://via.placeholder.com/50" },
      { name: "Product D", img: "https://via.placeholder.com/50" },
      { name: "Product E", img: "https://via.placeholder.com/50" },
    ],
    recentOrders: [
      {
        id: "12345",
        product: "Product A",
        img: "https://via.placeholder.com/50",
      },
      {
        id: "12346",
        product: "Product B",
        img: "https://via.placeholder.com/50",
      },
      {
        id: "12347",
        product: "Product C",
        img: "https://via.placeholder.com/50",
      },
    ],
  };

  // Update the dashboard with data
  document.getElementById(
    "total-sales-value"
  ).textContent = `$${data.totalSales.toLocaleString()}`;
  document.getElementById("total-orders-value").textContent =
    data.totalOrders.toLocaleString();
  document.getElementById(
    "average-order-value-value"
  ).textContent = `$${data.averageOrderValue.toFixed(2)}`;

  const topProductsList = document.getElementById("top-products-list");
  data.topProducts.forEach((product) => {
    const li = document.createElement("li");
    li.innerHTML = `<img src="${product.img}" alt="${product.name}"><span>${product.name}</span>`;
    topProductsList.appendChild(li);
  });

  const recentOrdersList = document.getElementById("recent-orders-list");
  data.recentOrders.forEach((order) => {
    const li = document.createElement("li");
    li.innerHTML = `<img src="${order.img}" alt="${order.product}"><span>Order #${order.id} - ${order.product}</span>`;
    recentOrdersList.appendChild(li);
  });
});
